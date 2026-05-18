# 🧪 Automated UI Testing Portfolio

## 📌 Project Overview
โปรเจกต์นี้เป็นการจำลองการทำ Automated UI Testing สำหรับทดสอบระบบเว็บไซต์ E-commerce เพื่อตรวจสอบความถูกต้องของฟังก์ชันการทำงานหลัก โดยใช้ **Python** และ **Playwright** ในการสร้างสคริปต์จำลองพฤติกรรมของผู้ใช้งานจริง

## 🛠️ Tools & Technologies
- **Language:** Python
- **Testing Framework:** Playwright (Pytest)
- **Target Website:** [Swag Labs (saucedemo.com)](https://www.saucedemo.com/)

---

## 📋 Test Scenarios & Test Cases

### 🎯 Scenario: ทดสอบระบบเข้าสู่ระบบ (Login System)

#### 📝 TC-LOG-001: ตรวจสอบการเข้าสู่ระบบด้วยบัญชีที่ถูกต้อง (Happy Path)
- **Pre-conditions:** อยู่ที่หน้า URL `https://www.saucedemo.com/`
- **Test Steps:**
  1. กรอก Username: `standard_user`
  2. กรอก Password: `secret_sauce`
  3. คลิกปุ่ม "Login"
- **Expected Result:** - ระบบเปลี่ยนไปยังหน้าสินค้า (URL มีคำว่า `/inventory.html`)
  - มีข้อความ "Products" แสดงอยู่บนหน้าจอ

#### 📝 TC-LOG-002: ตรวจสอบการเข้าสู่ระบบเมื่อกรอกรหัสผ่านผิด (Negative Test)
- **Pre-conditions:** อยู่ที่หน้า URL `https://www.saucedemo.com/`
- **Test Steps:**
  1. กรอก Username: `standard_user`
  2. กรอก Password: `wrong_password123`
  3. คลิกปุ่ม "Login"
- **Expected Result:** - ระบบไม่เปลี่ยนหน้า
  - มีข้อความ Error สีแดงแจ้งเตือนว่า *ล็อกอินไม่ถูกต้อง*