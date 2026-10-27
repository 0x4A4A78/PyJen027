# PyJen027

โปรแกรมบวกเลข Python สำหรับงาน Jenkins CI/CD เลขท้ายรหัสนักศึกษา 027

## Run

```console
python calculator.py
python calculator.py 12 30
python -m unittest discover -v
```

ใช้ Python standard library ไม่ต้องติดตั้ง package เพิ่ม

## Jenkins

สร้าง Pipeline job เลือก Pipeline script from SCM / Git ใส่ URL repository นี้
ตั้ง branch เป็น `*/main` และ Script Path เป็น `Jenkinsfile`
เครื่อง Jenkins ต้องมี Git และ Python ใน PATH แล้วกด Build Now ครั้งแรก

Jenkins จะตรวจสอบ GitHub ทุก 1 นาที เมื่อพบ commit ใหม่จะทำงานอัตโนมัติ:

1. Checkout โค้ดจาก GitHub
2. Build: ตรวจ syntax และสร้างไฟล์ `dist/calculator.py`
3. Test: ทดสอบการบวกและ command line ด้วย unittest
4. Deploy: คัดลอก artifact ไปยังโฟลเดอร์ `deploy` และตรวจผล `12 + 30 = 42`

นี่คือการ deploy โปรแกรม CLI ลงโฟลเดอร์ภายในเครื่อง Jenkins
ตั้ง environment variable `DEPLOY_DIR` เพื่อเปลี่ยนปลายทางได้
ถ้า test ไม่ผ่านจะไม่ deploy และไฟล์ build ที่สำเร็จดาวน์โหลดได้จาก Artifacts
Jenkins และเครื่องต้องเปิดอยู่เพื่อให้ตรวจสอบและ build อัตโนมัติ
