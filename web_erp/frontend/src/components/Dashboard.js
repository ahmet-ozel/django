import React, { Component } from "react";

export default class Dashboard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      meetingsData: [],
      speakingData: [],
      personsData: [],
    };
  }

  componentDidMount() {
    // API'den veriyi çekmek için fetch kullanımı
    const url = new URL("api/deneme/", window.location.origin);
    fetch(url) // API'nizin URL'sine uygun bir şekilde güncelleyin
      .then((response) => response.json())
      .then((data) => {
        this.setState({
          meetingsData: data.meetings_data,
          speakingData: data.speaking_data,
          personsData: data.persons_data,
        });
      })
      .catch((error) => {
        console.error("API hatası:", error);
      });
  }

  render() {
    return (
      <div>
        <h1>Hello from the Dashboard!</h1>
        <h2>Meetings Data:</h2>
        <ul>
          {this.state.meetingsData.map((meeting, index) => (
            <li key={index}>
              Meeting ID: {meeting.meeting_id}, Date: {meeting.meeting_date}, Time: {meeting.time}
              {/* Diğer verileri burada gösterebilirsiniz */}
            </li>
          ))}
        </ul>

        <h2>Speaking Data:</h2>
        <ul>
          {this.state.speakingData.map((speaking, index) => (
            <li key={index}>
              Meeting ID: {speaking.meeting_id}, Description: {speaking.description}, Speaker: {speaking.speaker}
              {/* Diğer verileri burada gösterebilirsiniz */}
            </li>
          ))}
        </ul>

        <h2>Persons Data:</h2>
        <ul>
          {this.state.personsData.map((person, index) => (
            <li key={index}>
              Person TC: {person.person_tc}, Name: {person.person_name}, Lastname: {person.person_lastname}, University: {person.university}
              {/* Diğer verileri burada gösterebilirsiniz */}
            </li>
          ))}
        </ul>
      </div>
    );
  }
}
