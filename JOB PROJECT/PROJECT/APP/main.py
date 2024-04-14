from fastapi import FastAPI , Body , Depends , HTTPException
from database import Base_dev , engine , SessionLocal_dev
from sqlalchemy.orm import Session 
from sqlalchemy import func , cast , and_, or_ , create_engine, text
from datetime import datetime , timedelta , date
import models
import schemas

app = FastAPI(
    title='FastAPI: EXAMPLE',
    description='Created by Diwjiw'
)

def get_sesion_dev():
    session_dev = SessionLocal_dev()
    try:
        yield session_dev
    finally:
        session_dev.close()
        
@app.get("/GET_DEV/RAW_QUERY/{item_id}", tags=["GET USER"])
async def getItem(item_id: int
                  ,session_dev: Session = Depends(get_sesion_dev)):
    try : 
        if item_id !=0:#CUSTOMER
            query = text("SELECT * FROM CUSTOMER.USER AS U WHERE U.USERID = :USERID")
        else :
            query = text("SELECT * FROM CUSTOMER.USER AS U WHERE U.USERID = 1")
            
        user = session_dev.execute(query, params={"USERID":item_id})
    
        result = [schemas.USER_TEST.from_orm(row) for row in user]
    
        return result

    except Exception as e:
        return {"message":f"An error occurred while querying the database: {str(e)}"}
    finally:
        session_dev.close

@app.get("/GET_DEV/DRM/{item_id}", tags=["Get Data"])
async def getItem(item_id:int
            ,session_dev: Session = Depends(get_sesion_dev)):
    
    try:
        if item_id !=0:
            user = session_dev.query(models.User).filter(models.User.USERID == item_id)
        else:
            user = session_dev.query(models.User).filter(models.User.USERID == 1)
        result = user.all()
    
        return result
    
    except Exception as e:
        return {"message": f"An error occurred while querying the database: {str(e)}"} 
    finally:
        session_dev.close
        result.clear
        
@app.post('/GET_DEV/CREATE/',tags=["CREATE USER"])
async def create_user(user_data: schemas.USER_TEST, session_dev: Session = Depends(get_sesion_dev)):
    try:
        user = models.User(**user_data.dict())
        session_dev.add(user)
        session_dev.commit()
        session_dev.refresh(user)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while creating the user: {str(e)}")
    finally:
        session_dev.close()
        
@app.post('/GET_DEV/CREATE_EMP/',tags=["CREATE EMPLOYEE"])
async def create_emp(emp_data: schemas.RESPONSE_TEST,session_dev:Session =Depends(get_sesion_dev)):
    try:
        emp = models.Emp(**emp_data.dict())
        session_dev.add(emp)
        session_dev.commit()
        session_dev.refresh(emp)
        return emp
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while creating the user: {str(e)}")
    finally:
        session_dev.close()
        
@app.delete('/GET_DEV/DELETE/{user_id}', tags=["Delete User"])
async def delete_user(user_id: int, session_dev: Session = Depends(get_sesion_dev)):
    try:
        user = session_dev.query(models.User).filter(models.User.USERID == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        session_dev.delete(user)
        session_dev.commit()
        return {"message": "User deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while deleting the user: {str(e)}")
    finally:
        session_dev.close()
    
@app.delete('/GET_DEV/DELETE_EMP/{emp_id}', tags=["Delete Employee"])
async def delete_emp(emp_id: int, session_dev: Session = Depends(get_sesion_dev)):
    try:
        emp = session_dev.query(models.Emp).filter(models.Emp.EMPID == emp_id).first()
        if not emp:
            raise HTTPException(status_code=404, detail="Employee not found")
        session_dev.delete(emp)
        session_dev.commit()
        return {"message": "Employee deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while deleting the employee: {str(e)}")
    finally:
        session_dev.close()
        
@app.put('/GET_DEV/UPDATE/{user_id}', tags=["Update User"])
async def update_user(user_id: int, user_data: schemas.USER_TEST, session_dev: Session = Depends(get_sesion_dev)):
    try:
        user = session_dev.query(models.User).filter(models.User.USERID == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        user.USERNAME = user_data.USERNAME
        user.PASSWORD = user_data.PASSWORD
        session_dev.commit()
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while updating the user: {str(e)}")
    finally:
        session_dev.close()
        
@app.put('/GET_DEV/UPDATE_EMP/{emp_id}', tags=["Update Employee"])
async def update_emp(emp_id: int, emp_data: schemas.RESPONSE_TEST, session_dev: Session = Depends(get_sesion_dev)):
    try:
        emp = session_dev.query(models.Emp).filter(models.Emp.EMPID == emp_id).first()
        if not emp:
            raise HTTPException(status_code=404, detail="Employee not found")
        emp.EMPNAME = emp_data.EMPNAME
        emp.EMPPASSWORD = emp_data.EMPPASSWORD
        session_dev.commit()
        return emp
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while updating the employee: {str(e)}")
    finally:
        session_dev.close()