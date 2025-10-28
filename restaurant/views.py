import json
from django.shortcuts import render, get_object_or_404
from pathlib import Path

# BASE_DIR คือ C:\website
BASE_DIR = Path(__file__).resolve().parent.parent 

def _load_restaurant_data():
    """ฟังก์ชันช่วยในการโหลดข้อมูลจาก JSON (ใช้ซ้ำสำหรับ index และ detail)"""
    json_file_path = BASE_DIR / 'restaurant' / 'mock_restaurants.json'
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: mock_restaurants.json file not found.")
        return []

def index(request):
    restaurant_data = _load_restaurant_data()
    
    # 3. ส่งข้อมูลไปยัง Template
    context = {
        'restaurants': restaurant_data, 
        'api_source': 'Mock API Data from Ratchaburi'
    }
    return render(request, 'index.html', context)


# 🌟🌟🌟 NEW: ฟังก์ชันสำหรับแสดงหน้ารายละเอียด 🌟🌟🌟
def detail(request, restaurant_id):
    # 1. โหลดข้อมูลทั้งหมด
    restaurants = _load_restaurant_data()
    
    # 2. ค้นหาร้านอาหารตาม ID (จำลองการดึงจากฐานข้อมูล)
    # ใช้ next() เพื่อค้นหาร้านแรกที่ตรงเงื่อนไข
    try:
        # restaurant_id จาก URL เป็น integer
        restaurant = next(item for item in restaurants if item["id"] == restaurant_id)
    except StopIteration:
        # ถ้าหา ID ไม่เจอ ให้โยน Error 404 (Not Found)
        return render(request, '404.html', status=404) # ต้องสร้าง 404.html เอง หรือใช้ get_object_or_404 ถ้าใช้ Model
    
    # 3. ส่งข้อมูลร้านที่พบไปยัง Template
    context = {
        'restaurant': restaurant,
        # 🌟 เพิ่มข้อมูลรูปภาพอาหาร (ใช้ image_url ตัวเดิมจำลองเป็นรูปภาพอาหาร)
        'food_images': [restaurant['image_url'], restaurant['image_url'], restaurant['image_url']] # ทำซ้ำ 3 ครั้งเพื่อจำลองรูปอาหารเพิ่มเติม
    }
    return render(request, 'detail.html', context)