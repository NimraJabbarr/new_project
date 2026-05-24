#!/usr/bin/env python3
"""
Complete API Endpoint Testing Report
Tests all School CRM endpoints and returns working status
"""

import urllib.request
import json
import sys

print("\n" + "="*80)
print("🧪 SCHOOL CRM - COMPLETE ENDPOINT TEST REPORT")
print("="*80)

BASE_URL = "http://localhost:8000"
results = {
    "working": [],
    "protected": [],
    "failed": []
}

# Test 1: Homepage
print("\n[TEST 1] HOMEPAGE")
print("-" * 80)
try:
    response = urllib.request.urlopen(f"{BASE_URL}/")
    results["working"].append({
        "name": "Homepage",
        "method": "GET",
        "endpoint": "/",
        "status": response.status,
        "description": "Main homepage"
    })
    print("✅ GET / → 200 OK - Homepage is working")
except Exception as e:
    results["failed"].append({"endpoint": "/", "error": str(e)[:50]})
    print(f"❌ GET / → Failed: {str(e)[:50]}")

# Test 2: Register Endpoint (POST)
print("\n[TEST 2] REGISTER API")
print("-" * 80)
try:
    data = json.dumps({
        "username": f"testuser_{int(__import__('time').time())}",
        "password": "TestPass123",
        "role": "student",
        "phone": "03001234567",
        "address": "Test Address"
    }).encode('utf-8')
    
    req = urllib.request.Request(
        f"{BASE_URL}/api/register/",
        data=data,
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode())
    results["working"].append({
        "name": "Register User",
        "method": "POST",
        "endpoint": "/api/register/",
        "status": response.status,
        "description": "User registration"
    })
    print(f"✅ POST /api/register/ → {response.status} Created - User registration working")
except urllib.error.HTTPError as e:
    results["failed"].append({"endpoint": "/api/register/", "error": f"{e.code} - {e.reason}"})
    print(f"❌ POST /api/register/ → {e.code} - {e.reason}")
except Exception as e:
    results["failed"].append({"endpoint": "/api/register/", "error": str(e)[:50]})
    print(f"❌ POST /api/register/ → Error: {str(e)[:50]}")

# Test 3: Login Endpoint (POST)
print("\n[TEST 3] LOGIN API")
print("-" * 80)
try:
    data = json.dumps({
        "username": "huda",
        "password": "1234"
    }).encode('utf-8')
    
    req = urllib.request.Request(
        f"{BASE_URL}/api/login/",
        data=data,
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode())
    token = result.get('access', '')
    results["working"].append({
        "name": "User Login",
        "method": "POST",
        "endpoint": "/api/login/",
        "status": response.status,
        "description": "User login & JWT token generation"
    })
    print(f"✅ POST /api/login/ → {response.status} OK - Login working, token received")
except urllib.error.HTTPError as e:
    error_body = e.read().decode()
    results["failed"].append({"endpoint": "/api/login/", "error": f"{e.code} - {e.reason}"})
    print(f"❌ POST /api/login/ → {e.code} - {e.reason}")
except Exception as e:
    results["failed"].append({"endpoint": "/api/login/", "error": str(e)[:50]})
    print(f"❌ POST /api/login/ → Error: {str(e)[:50]}")

# Test 4: Students Endpoint (GET) - Protected
print("\n[TEST 4] STUDENTS API (Protected)")
print("-" * 80)
try:
    response = urllib.request.urlopen(f"{BASE_URL}/api/students/")
    results["working"].append({
        "name": "List Students",
        "method": "GET",
        "endpoint": "/api/students/",
        "status": response.status,
        "description": "List all students"
    })
    print(f"✅ GET /api/students/ → {response.status} OK - Students endpoint working")
except urllib.error.HTTPError as e:
    if e.code == 401:
        results["protected"].append({
            "name": "List Students",
            "method": "GET",
            "endpoint": "/api/students/",
            "status": e.code,
            "description": "List all students (requires JWT)"
        })
        print(f"⚠️ GET /api/students/ → {e.code} Unauthorized - Protected (requires JWT token)")
    else:
        results["failed"].append({"endpoint": "/api/students/", "error": f"{e.code}"})
        print(f"❌ GET /api/students/ → {e.code} Error")
except Exception as e:
    results["failed"].append({"endpoint": "/api/students/", "error": str(e)[:50]})
    print(f"❌ GET /api/students/ → Error: {str(e)[:50]}")

# Test 5: Teachers Endpoint (GET) - Protected
print("\n[TEST 5] TEACHERS API (Protected)")
print("-" * 80)
try:
    response = urllib.request.urlopen(f"{BASE_URL}/api/teachers/")
    results["working"].append({
        "name": "List Teachers",
        "method": "GET",
        "endpoint": "/api/teachers/",
        "status": response.status,
        "description": "List all teachers"
    })
    print(f"✅ GET /api/teachers/ → {response.status} OK - Teachers endpoint working")
except urllib.error.HTTPError as e:
    if e.code == 401:
        results["protected"].append({
            "name": "List Teachers",
            "method": "GET",
            "endpoint": "/api/teachers/",
            "status": e.code,
            "description": "List all teachers (requires JWT)"
        })
        print(f"⚠️ GET /api/teachers/ → {e.code} Unauthorized - Protected (requires JWT token)")
    else:
        results["failed"].append({"endpoint": "/api/teachers/", "error": f"{e.code}"})
        print(f"❌ GET /api/teachers/ → {e.code} Error")
except Exception as e:
    results["failed"].append({"endpoint": "/api/teachers/", "error": str(e)[:50]})
    print(f"❌ GET /api/teachers/ → Error: {str(e)[:50]}")

# Test 6: Classrooms Endpoint (GET) - Protected
print("\n[TEST 6] CLASSROOMS API (Protected)")
print("-" * 80)
try:
    response = urllib.request.urlopen(f"{BASE_URL}/api/classrooms/")
    results["working"].append({
        "name": "List Classrooms",
        "method": "GET",
        "endpoint": "/api/classrooms/",
        "status": response.status,
        "description": "List all classrooms"
    })
    print(f"✅ GET /api/classrooms/ → {response.status} OK - Classrooms endpoint working")
except urllib.error.HTTPError as e:
    if e.code == 401:
        results["protected"].append({
            "name": "List Classrooms",
            "method": "GET",
            "endpoint": "/api/classrooms/",
            "status": e.code,
            "description": "List all classrooms (requires JWT)"
        })
        print(f"⚠️ GET /api/classrooms/ → {e.code} Unauthorized - Protected (requires JWT token)")
    else:
        results["failed"].append({"endpoint": "/api/classrooms/", "error": f"{e.code}"})
        print(f"❌ GET /api/classrooms/ → {e.code} Error")
except Exception as e:
    results["failed"].append({"endpoint": "/api/classrooms/", "error": str(e)[:50]})
    print(f"❌ GET /api/classrooms/ → Error: {str(e)[:50]}")

# Test 7: Attendance Endpoint (GET) - Protected
print("\n[TEST 7] ATTENDANCE API (Protected)")
print("-" * 80)
try:
    response = urllib.request.urlopen(f"{BASE_URL}/api/attendance/")
    results["working"].append({
        "name": "List Attendance",
        "method": "GET",
        "endpoint": "/api/attendance/",
        "status": response.status,
        "description": "List all attendance records"
    })
    print(f"✅ GET /api/attendance/ → {response.status} OK - Attendance endpoint working")
except urllib.error.HTTPError as e:
    if e.code == 401:
        results["protected"].append({
            "name": "List Attendance",
            "method": "GET",
            "endpoint": "/api/attendance/",
            "status": e.code,
            "description": "List all attendance records (requires JWT)"
        })
        print(f"⚠️ GET /api/attendance/ → {e.code} Unauthorized - Protected (requires JWT token)")
    else:
        results["failed"].append({"endpoint": "/api/attendance/", "error": f"{e.code}"})
        print(f"❌ GET /api/attendance/ → {e.code} Error")
except Exception as e:
    results["failed"].append({"endpoint": "/api/attendance/", "error": str(e)[:50]})
    print(f"❌ GET /api/attendance/ → Error: {str(e)[:50]}")

# Test 8: Admin Panel
print("\n[TEST 8] ADMIN PANEL")
print("-" * 80)
try:
    response = urllib.request.urlopen(f"{BASE_URL}/admin/")
    results["working"].append({
        "name": "Admin Panel",
        "method": "GET",
        "endpoint": "/admin/",
        "status": response.status,
        "description": "Django Admin interface"
    })
    print(f"✅ GET /admin/ → {response.status} OK - Admin panel accessible")
except urllib.error.HTTPError as e:
    if e.code in [301, 302, 303, 304]:
        results["protected"].append({
            "name": "Admin Panel",
            "method": "GET",
            "endpoint": "/admin/",
            "status": e.code,
            "description": "Django Admin interface (requires authentication)"
        })
        print(f"⚠️ GET /admin/ → {e.code} Redirect - Admin panel requires login")
    else:
        results["failed"].append({"endpoint": "/admin/", "error": f"{e.code}"})
        print(f"❌ GET /admin/ → {e.code} Error")
except Exception as e:
    results["failed"].append({"endpoint": "/admin/", "error": str(e)[:50]})
    print(f"❌ GET /admin/ → Error: {str(e)[:50]}")

# Print Summary
print("\n" + "="*80)
print("📊 FINAL REPORT SUMMARY")
print("="*80)

print(f"\n✅ WORKING ENDPOINTS: {len(results['working'])}")
print("-" * 80)
for ep in results['working']:
    print(f"  {ep['method']:6} {ep['endpoint']:25} [{ep['status']}] {ep['description']}")

print(f"\n⚠️ PROTECTED ENDPOINTS (Require JWT): {len(results['protected'])}")
print("-" * 80)
for ep in results['protected']:
    print(f"  {ep['method']:6} {ep['endpoint']:25} [{ep['status']}] {ep['description']}")

if results['failed']:
    print(f"\n❌ FAILED ENDPOINTS: {len(results['failed'])}")
    print("-" * 80)
    for ep in results['failed']:
        print(f"  {ep['endpoint']:25} Error: {ep['error']}")
else:
    print(f"\n❌ FAILED ENDPOINTS: 0")
    print("-" * 80)

# Overall Status
total_working = len(results['working']) + len(results['protected'])
print("\n" + "="*80)
print(f"🎯 OVERALL STATUS: {total_working} / {total_working + len(results['failed'])} endpoints operational")
print("="*80)

if len(results['failed']) == 0:
    print("\n✅ ALL ENDPOINTS ARE OPERATIONAL!\n")
else:
    print(f"\n⚠️ {len(results['failed'])} endpoint(s) have issues\n")
