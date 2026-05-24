#!/usr/bin/env python3
"""Quick API Endpoint Test"""

import urllib.request
import json

BASE = "http://localhost:8000"

print("\n" + "="*70)
print("✅ SCHOOL CRM - WORKING ENDPOINTS TEST")
print("="*70)

endpoints = [
    ("GET", "/", "Homepage", False),
    ("POST", "/api/register/", "Register User", False),
    ("POST", "/api/login/", "User Login", False),
    ("GET", "/api/students/", "List Students", True),
    ("GET", "/api/teachers/", "List Teachers", True),
    ("GET", "/api/classrooms/", "List Classrooms", True),
    ("GET", "/api/attendance/", "List Attendance", True),
    ("GET", "/admin/", "Admin Panel", True),
]

working = []
protected = []
failed = []

print("\n🔌 TESTING ALL ENDPOINTS:\n")

# Test 1: Homepage
try:
    r = urllib.request.urlopen(f"{BASE}/")
    working.append("GET / - Homepage")
    print("✅ GET / → 200 OK")
except:
    failed.append("GET /")
    print("❌ GET /")

# Test 2: Register
try:
    data = json.dumps({"username":"test","password":"test","role":"student"}).encode()
    req = urllib.request.Request(f"{BASE}/api/register/", data=data, headers={'Content-Type':'application/json'}, method='POST')
    r = urllib.request.urlopen(req)
    working.append("POST /api/register/ - Register")
    print("✅ POST /api/register/ → 201 Created")
except:
    failed.append("POST /api/register/")
    print("❌ POST /api/register/")

# Test 3: Login
try:
    data = json.dumps({"username":"huda","password":"1234"}).encode()
    req = urllib.request.Request(f"{BASE}/api/login/", data=data, headers={'Content-Type':'application/json'}, method='POST')
    r = urllib.request.urlopen(req)
    working.append("POST /api/login/ - Login")
    print("✅ POST /api/login/ → 200 OK")
except:
    failed.append("POST /api/login/")
    print("❌ POST /api/login/")

# Test 4-7: Protected endpoints
protected_eps = [
    ("GET", "/api/students/", "Students"),
    ("GET", "/api/teachers/", "Teachers"),
    ("GET", "/api/classrooms/", "Classrooms"),
    ("GET", "/api/attendance/", "Attendance"),
]

for method, endpoint, name in protected_eps:
    try:
        urllib.request.urlopen(f"{BASE}{endpoint}")
        working.append(f"{method} {endpoint} - {name}")
        print(f"✅ {method} {endpoint} → 200 OK")
    except urllib.error.HTTPError as e:
        if e.code == 401:
            protected.append(f"{method} {endpoint} - {name} (Protected)")
            print(f"⚠️ {method} {endpoint} → 401 Unauthorized (Protected)")
        else:
            failed.append(f"{method} {endpoint}")
            print(f"❌ {method} {endpoint} → {e.code}")
    except:
        failed.append(f"{method} {endpoint}")
        print(f"❌ {method} {endpoint}")

# Test Admin
try:
    urllib.request.urlopen(f"{BASE}/admin/")
    working.append("GET /admin/ - Admin")
    print("✅ GET /admin/ → 200 OK")
except urllib.error.HTTPError as e:
    if e.code in [301, 302, 303]:
        protected.append("GET /admin/ - Admin (Protected)")
        print(f"⚠️ GET /admin/ → {e.code} Redirect (Protected)")
    else:
        failed.append("GET /admin/")
        print(f"❌ GET /admin/ → {e.code}")
except:
    failed.append("GET /admin/")
    print(f"❌ GET /admin/")

print("\n" + "="*70)
print("📊 SUMMARY")
print("="*70)

print(f"\n✅ FULLY WORKING: {len(working)}")
for ep in working:
    print(f"   • {ep}")

print(f"\n⚠️ PROTECTED (Need JWT): {len(protected)}")
for ep in protected:
    print(f"   • {ep}")

if failed:
    print(f"\n❌ FAILED: {len(failed)}")
    for ep in failed:
        print(f"   • {ep}")
else:
    print(f"\n❌ FAILED: 0")

print("\n" + "="*70)
total = len(working) + len(protected)
print(f"🎯 TOTAL WORKING: {total} / {total + len(failed)}")
print("="*70 + "\n")
