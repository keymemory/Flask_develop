from pybo import db
from pybo.models import Question
from datetime import datetime
for i in range(300):
    q = Question(subject='테스트 데이터입니다:[%03d]' % i, content='내용무', create_date=datetime.now())
    db.session(q)
db.session.commit()