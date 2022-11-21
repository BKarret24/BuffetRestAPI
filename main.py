from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import order_handler
from database import SessionLocal, init_models

init_models()
app = FastAPI()
students = [
    {'name': 'Student 1', 'age': 20},
    {'name': 'Student 2', 'age': 18},
    {'name': 'Student 3', 'age': 16}
]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/orders")
async def get_orders(user_name: str, db: Session = Depends(get_db)):
    orders = order_handler.get_orders()
    print(orders)
    return orders


'''@app.post('/api/orders')
def user_add(order: Order, db: Session = Depends(get_db)):
    db.add(order)
    db.commit()
    db.refresh(order)
    return order'''


'''class Student(BaseModel):
    name: str
    age: int


@app.get('/students')
def user_list(min: Optional[int] = None, max: Optional[int] = None):
    if min and max:
        filtered_students = list(
            filter(lambda student: max >= student['age'] >= min, students)
        )

        return {'students': filtered_students}

    return {'students': students}


@app.get('/students/{student_id}')
def user_detail(student_id: int):
    student_check(student_id)
    return {'student': students[student_id]}


@app.post('/students')
def user_add(student: Student):
    students.append(student)

    return {'student': students[-1]}


@app.put('/students/{student_id}')
def user_update(student: Student, student_id: int):
    student_check(student_id)
    students[student_id].update(student)

    return {'student': students[student_id]}


@app.delete('/students/{student_id}')
def user_delete(student_id: int):
    student_check(student_id)
    del students[student_id]

    return {'students': students}


def student_check(student_id):
    if not students[student_id]:
        raise HTTPException(status_code=404, detail='Student Not Found')


@app.get("/")
async def root():
    return {"message": "Hello World"}'''
