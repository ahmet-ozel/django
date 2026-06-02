# Web ERP — Çok Şirketli Toplantı & CRM Platformu

[![Django](https://img.shields.io/badge/Django-REST-092E20?logo=django&logoColor=white)](https://www.djangoproject.com)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)
[![React](https://img.shields.io/badge/React-17-61DAFB?logo=react&logoColor=black)](https://react.dev)
[![Material UI](https://img.shields.io/badge/Material--UI-4-0081CB?logo=mui&logoColor=white)](https://mui.com)
[![Webpack](https://img.shields.io/badge/Webpack-5-8DD6F9?logo=webpack&logoColor=black)](https://webpack.js.org)

Django + React tabanlı, çok şirketli (multi-tenant) bir toplantı yönetimi ve müşteri ilişkileri (CRM) uygulaması. Şirketler kendi kullanıcılarını ve kişilerini yönetir, toplantı kayıtları tutulur ve toplantılara ait analiz sonuçları (duygu, yaş, cinsiyet tahmini gibi) veritabanında saklanır.

> Not: Bu proje bir öğrenme/portföy projesidir. Django REST backend ile webpack üzerinden derlenen bir React frontend'in tek bir projede nasıl birleştirildiğini gösterir.

## Özellikler

- Çok şirketli yapı — her `Company` kendi kullanıcılarına ve verisine sahip
- `AbstractUser` üzerine kurulu özel kullanıcı modeli (`CustomUser`) ve özel `UserManager`
- Kişi (`Person`) ve toplantı (`Meeting`) yönetimi
- Toplantı analiz sonuçlarının saklanması (`MeetingDescription`: duygu, yaş, cinsiyet, doğruluk skoru)
- Django admin paneli üzerinden veri yönetimi
- React + Material-UI ile tek sayfa (SPA) arayüz, webpack ile derlenir

## Teknoloji Yığını

| Katman | Teknoloji |
|---|---|
| Backend | Django, Django REST Framework |
| Frontend | React 17, Material-UI 4, React Router, Axios |
| Build | Webpack 5, Babel |
| Veritabanı | SQLite (geliştirme) |

## Proje Yapısı

```
web_erp/
├── manage.py
├── web_erp/          # Django proje ayarları (settings, urls, wsgi)
├── api/              # REST API uygulaması — modeller, view'lar, migration'lar
│   ├── models.py     # Company, CustomUser, Person, Meeting, MeetingDescription
│   ├── views.py
│   └── urls.py
└── frontend/         # React uygulaması (webpack ile derlenir)
    ├── src/          # React bileşenleri
    ├── static/       # Derlenmiş çıktı (main.js)
    ├── package.json
    └── webpack.config.js
```

## Kurulum

### Backend

```bash
cd web_erp
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

pip install django djangorestframework
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Uygulama varsayılan olarak `http://127.0.0.1:8000` adresinde çalışır.

### Frontend

```bash
cd web_erp/frontend
npm install

# Geliştirme (dosya değişikliklerini izler)
npm run dev

# Üretim derlemesi
npm run build
```

`npm run dev` webpack'i watch modunda çalıştırır ve React kaynağını `static/frontend/main.js` dosyasına derler; Django bunu template üzerinden servis eder.

## Veri Modeli (özet)

- **Company** — Şirket bilgisi (abonelik tarihi, telefon vb.)
- **CustomUser** — Şirkete bağlı özel kullanıcı modeli
- **Person** — Toplantıya katılan kişi
- **Meeting** — Şirket, kullanıcı ve kişiyi ilişkilendiren toplantı kaydı
- **MeetingDescription** — Toplantı analiz sonuçları (duygu, yaş, cinsiyet, doğruluk)

## Lisans

Bu proje öğrenme amaçlıdır ve eğitim/portföy kullanımı için paylaşılmıştır.
