from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(tags=["Students"])

# ------------------------ GET ALL STUDENTS ------------------------


@router.get("/v1/students", response_model=List[schemas.ResponseData])
def get_all_students(
    db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)
):
    students_data = db.query(models.Students).all()
    print(current_user.email)
    return students_data


# ------------------------ ADD NEW STUDENT ------------------------


@router.post(
    "/v1/students",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.ResponseData,
)
def add_student(
    student: schemas.CreateStudent,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    new_student = models.Students(
        owner_id=current_user.id, **student.dict()
    )  # Makes sure we dont have to add every field one by one.
    db.add(new_student)
    db.commit()
    db.refresh(
        new_student
    )  # Takes the newly created user and adds it back in the variable new_student
    return new_student


# ------------------------ GET STUDENT WITH ID ------------------------


@router.get(
    "/v1/students/{id}", response_model=schemas.ResponseData
)  # ID comes in as a string
def get_student(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    student = (
        db.query(models.Students).filter(models.Students.id == id).first()
    )  # will change the first match it finds. \
    # can be .all() as well if all needs to be changed.
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error: Not Found. No student with id: {id}",
        )
    return student


# ------------------------ DELETE STUDENT RECORD ------------------------


@router.delete("/v1/students/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    deleted_student_query = db.query(models.Students).filter(models.Students.id == id)
    deleted_student = deleted_student_query.first()
    if deleted_student == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error: Not Found. No student with id: {id}",
        )
    if deleted_student.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Error: User(Owner) {current_user.id} is not authorized to remove user {deleted_student.id}",
        )
    deleted_student_query.delete(synchronize_session=False)
    db.commit()


# Nothing to return as 204 NO CONTENT.


# ------------------------ UPDATE EXISTING STUDENT INFORMATION ------------------------


@router.put("/v1/students/{id}", response_model=schemas.ResponseData)
def update_student(
    id: int,
    student: schemas.CreateStudent,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    update_query = db.query(models.Students).filter(models.Students.id == id)
    updated_student = update_query.first()
    if updated_student == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error: Not Found. No student with id: {id}",
        )
    if updated_student.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Error: User(Owner) {current_user.id} is not authorized to update user {updated_student.id}",
        )
    update_query.update(student.dict(), synchronize_session=False)
    db.commit()
    return update_query.first()
