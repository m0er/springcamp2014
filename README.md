내가 스프링을 선택한 이유 데모
===========================

발표 때 라이브코딩 못했던 부분도 추가했습니다.
커밋된 코드만 보면 디비에 데이터 넣는 부분이 보이지 않는데요.
제가 발표 때 준비했던 코드도 첨부합니다.
참고로 `django_extensions` 설치 후에 쉘은 쉘 플러스를 사용했습니다.

    python manage.py shell_plus

## 연사 추가
```python
new_speaker = Speaker()
new_speaker.name = 'mOer'
new_speaker.email = 'ethdemor@gmail.com'
new_speaker.save()
```

## 연사 확인
```python
speakers = Speaker.objects.all()
speakers
```

## 연사 업데이트
```python
speaker = Speaker.objects.get(name='mOer')
speaker.desc = 'foobar'
speaker.save()
```

## 세션 추가
```python
speaker = Speaker.objects.get(name='mOer')
Session.objects.create(title='Why I chose the python', desc='foobar', speaker=speaker)
Session.objects.all()
```
