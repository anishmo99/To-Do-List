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

while (True):
    print("1) Today's tasks")
    print("2) Add task")
    print("0) Exit")
    n = int(input())

    if n == 0:
        print("Bye!")
        break;

    count = 1

    if n == 1:
        tasks = session.query(task).all()

        for task_x in tasks:
            print("{0}. {1}".format(count, task_x))
            count += 1
        if count == 1:
            print("Nothing to do!")

    if n == 2:
        print("Enter task")
        task_new = input()
        new_task = task(task=task_new)
        session.add(new_task)
        session.commit()
        print("The task has been added!")