from sqlalchemy import create_engine
engine = create_engine('sqlite:///list.db?check_same_thread=False')

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime

Base = declarative_base()

class task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

from datetime import datetime,timedelta

today=datetime.today().date()
rows=session.query(task).filter(task.deadline==today).all()

while (True):

    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Add task")
    print("0) Exit")

    n = int(input())

    if n == 0:
        print("Bye!")
        break;

    if n == 1:

        count = 1

        tasks = session.query(task).filter(task.deadline == datetime.today().date()).all()

        for task_today in tasks:
            print("{0}. {1}".format(count, task_today))
            count += 1
        if count == 1:
            print("Nothing to do!")

    if n == 2:

        count = 1

        tasks = session.query(task).filter(task.deadline == datetime.today().date() + timedelta(days=7)).all()

        for task_week in tasks:
            print("{0}. {1}".format(count, task_week))
            count += 1
        if count == 1:
            print("Nothing to do!")

    if n == 3:

        count = 1

        tasks = session.query(task).all()

        for task_x in tasks:
            print("{0}. {1}".format(count, task_x))
            count += 1

        if count == 1:
            print("Nothing to do!")

    if n == 4:
        print("Enter activity")
        activity = input()

        print("Enter deadline")
        activity_deadline_str = input()
        activity_deadline = datetime.strptime(activity_deadline_str, '%Y-%m-%d').date()

        new_task = task(task=activity, deadline=activity_deadline)

        session.add(new_task)
        session.commit()

        print("The task has been added!")