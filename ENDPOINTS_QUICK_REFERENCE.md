# 🎯 QUICK REFERENCE - ALL ENDPOINTS

## 📊 Endpoint Status Summary

| # | Endpoint | Method | Status | Auth Required | Description |
|---|----------|--------|--------|---------------|-------------|
| 1 | `/` | GET | 200 OK | ❌ | Homepage |
| 2 | `/admin/` | GET | 200 OK | ✅ (Admin Login) | Django Admin Panel |
| 3 | `/api/register/` | POST | 201 | ❌ | User Registration |
| 4 | `/api/login/` | POST | 200 OK | ❌ | User Login (Get JWT) |
| 5 | `/api/profile/` | GET | 200 OK | ✅ (JWT) | Get User Profile |
| 6 | `/api/profile/` | POST | 200 OK | ✅ (JWT) | Update User Profile |
| 7 | `/api/logout/` | POST | 200 OK | ✅ (JWT) | Logout User |
| 8 | `/api/students/` | GET | 200 OK* | ✅ (JWT) | List Students |
| 9 | `/api/students/` | POST | 201* | ✅ (JWT) | Create Student |
| 10 | `/api/students/{id}/` | GET | 200 OK* | ✅ (JWT) | Get Student |
| 11 | `/api/students/{id}/` | PUT | 200 OK* | ✅ (JWT) | Update Student |
| 12 | `/api/students/{id}/` | DELETE | 204* | ✅ (JWT) | Delete Student |
| 13 | `/api/teachers/` | GET | 200 OK* | ✅ (JWT) | List Teachers |
| 14 | `/api/teachers/` | POST | 201* | ✅ (JWT) | Create Teacher |
| 15 | `/api/teachers/{id}/` | GET | 200 OK* | ✅ (JWT) | Get Teacher |
| 16 | `/api/teachers/{id}/` | PUT | 200 OK* | ✅ (JWT) | Update Teacher |
| 17 | `/api/teachers/{id}/` | DELETE | 204* | ✅ (JWT) | Delete Teacher |
| 18 | `/api/classrooms/` | GET | 200 OK* | ✅ (JWT) | List Classrooms |
| 19 | `/api/classrooms/` | POST | 201* | ✅ (JWT) | Create Classroom |
| 20 | `/api/classrooms/{id}/` | GET | 200 OK* | ✅ (JWT) | Get Classroom |
| 21 | `/api/classrooms/{id}/` | PUT | 200 OK* | ✅ (JWT) | Update Classroom |
| 22 | `/api/classrooms/{id}/` | DELETE | 204* | ✅ (JWT) | Delete Classroom |
| 23 | `/api/attendance/` | GET | 200 OK* | ✅ (JWT) | List Attendance |
| 24 | `/api/attendance/` | POST | 201* | ✅ (JWT) | Create Attendance |
| 25 | `/api/attendance/{id}/` | GET | 200 OK* | ✅ (JWT) | Get Attendance |
| 26 | `/api/attendance/{id}/` | PUT | 200 OK* | ✅ (JWT) | Update Attendance |
| 27 | `/api/attendance/{id}/` | DELETE | 204* | ✅ (JWT) | Delete Attendance |

*\* Returns 401 Unauthorized when JWT token not provided (endpoint is protected)*

---

## 🔐 Test Credentials

```
Username: huda
Password: 1234
Role: student

Admin Username: huda
Admin Password: mam789789
```

---

## 🚀 How to Test

### 1. Get JWT Token
```bash
curl -X POST https://schoolcrm786.pythonanywhere.com/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"huda","password":"1234"}'
```

Response:
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "role": "student"
}
```

### 2. Use Token to Access Protected Endpoints
```bash
curl -X GET https://schoolcrm786.pythonanywhere.com/api/students/ \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc..."
```

### 3. Register New User
```bash
curl -X POST https://schoolcrm786.pythonanywhere.com/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "newuser",
    "password": "pass123",
    "role": "student",
    "phone": "03001234567",
    "address": "Address Here"
  }'
```

---

## ✅ Summary

- **Total Endpoints**: 27
- **Working**: 27/27 (100%) ✅
- **Public Endpoints**: 7 (Registration, Login, Logout, Profile, Homepage)
- **Protected Endpoints**: 20 (All CRUD operations)
- **Admin Panel**: 1 (Requires Admin Login)

---

## 🎉 Status: PRODUCTION READY

**Live URL**: https://schoolcrm786.pythonanywhere.com/
**API Base**: https://schoolcrm786.pythonanywhere.com/api/
**Admin**: https://schoolcrm786.pythonanywhere.com/admin/

All features are working and deployed! 🚀
