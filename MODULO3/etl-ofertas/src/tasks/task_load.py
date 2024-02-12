from prefect import task
import sqlite3
from sqlalchemy import create_engine,Column,Integer,String,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import asyncio

Base = declarative_base()

class Oferta(Base):
   __tablename__ = 'ofertas'
   id = Column(Integer,primary_key=True)
   puesto = Column(String)
   ubicacion = Column(String)
   url = Column(String)
   fecha = Column(Date)
   
   

@task(name="CARGANDO LA DATA EN LA BASE DE DATOS...")
async def task_load(ofertas):
   engine = create_engine('sqlite:///ofertas.db',echo=True)
   Base.metadata.create_all(bind=engine)
   Session = sessionmaker(bind=engine)
   session = Session()
   
   for oferta in ofertas:
      nueva_oferta = Oferta(
         puesto=oferta['puesto'],
         ubicacion=oferta['ubicacion'],
         url=oferta['url'],
         fecha=datetime.strptime(oferta['fecha'],'%Y-%m-%d').date()
      )
      session.add(nueva_oferta)
      
   session.commit()
   session.close()
    