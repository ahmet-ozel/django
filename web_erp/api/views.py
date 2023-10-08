from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from api.models import Meeting, SpeakingDescription, Person, MeetingDescription

class DenemeView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            user_id = request.user.id  # Kullanıcının kimliğini alın

            # Kullanıcının toplantıları
            meetings_data = Meeting.objects.filter(userid=user_id)

            # MeetingDescription tablosunu filtreleyin ve ilgili alanları alın
            combined_data = MeetingDescription.objects.filter(meeting_id__in=meetings_data).values(
                'meeting_id__meeting_id', 'meeting_id__meeting_date', 'time',
                'gender', 'age', 'emotion', 'precisions',
                'meeting_id__person_tc', 'meeting_id__person_name'
            )

            # Verileri düzgün bir şekilde formatlayın
            result_data = []
            for item in combined_data:
                result_data.append({
                    'meeting_id': item['meeting_id__meeting_id'],
                    'meeting_date': item['meeting_id__meeting_date'],
                    'time': item['time'],
                    'gender': item['gender'],
                    'age': item['age'],
                    'emotion': item['emotion'],
                    'precisions': item['precisions'],
                    'person_tc': item['meeting_id__person_tc'],
                    'person_name': item['meeting_id__person_name'],
                })

            # SpeakingDescription verilerini düzgün bir şekilde formatlayın
            speaking_data = SpeakingDescription.objects.filter(meeting_id__in=meetings_data).values(
                'meeting_id__meeting_id', 'description', 'speaker', 'start_time', 'end_time'
            )
            speaking_datas = []
            for item in speaking_data:
                speaking_datas.append({
                    'meeting_id': item['meeting_id__meeting_id'],
                    'description': item['description'],
                    'speaker': item['speaker'],
                    'start_time': item['start_time'],
                    'end_time': item['end_time'],
                })

            # Person verilerini düzgün bir şekilde formatlayın
            person_data = Person.objects.filter(person_tc__in=combined_data.values('meeting_id__person_tc'))
            persons_list = []
            for person in person_data:
                persons_list.append({
                    "person_tc": person.person_tc,
                    "person_name": person.person_name,
                    "person_lastname": person.person_lastname,
                    "university": person.university,
                })

            # JSON yanıtını oluşturun
            response_data = {
                "meetings_data": result_data,
                "speaking_data": speaking_datas,
                "persons_data": persons_list,
            }

            return Response(response_data)
