## 환경 세팅
가상환경 설치 후 진행 권장
- 가상환경 생성방법
```
python3 -m venv 가상환경명
```
- 가상환경 접속방법
```
source 가상환경명/bin/activate
```
- 가상환경 종료방법
```
deactivate
```

## 설치 패키지 
```
pip install -r requirements.txt
```

## 실행 구문 

Run the database (if needed) using the provided Makefile command:
```
make run-db
```

Run the API with Uvicorn:
```
uvicorn src.main:app --reload
```

Run the database migration:
```
alembic upgrade head
```

Hit the POST endpoint with cURL:
```
curl --request POST --data '{"title": "my first job", "description": "an awesome job"}' localhost:8000
```

Hit the GET endpoint:
```
curl --request GET "localhost:8000?id=1"
```

Hit the DELETE endpoint:
```
curl --request DELETE "localhost:8000?id=1"
```