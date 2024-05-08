
"use client"
import Image from 'next/image';
import { Calendar } from 'primereact/calendar';
import { InputText } from 'primereact/inputtext';
import { Button } from 'primereact/button';
import { InputMask } from 'primereact/inputmask';
import { InputNumber } from 'primereact/inputnumber';




import React, { useState } from "react";


function categories() {

  const arr = []

  for (let i = 0; i < 100; i++) {
    arr.push(
      <li className="category">
      <Image
      
      src="/categorias/cabine.svg"
      alt="categoria"
      width={14}
      height={14}
      
      />
      <label>Cabine</label>
      </li>
    )   
  }

  return arr;

}


function commodities() {

  const arr = []

  for (let i = 0; i < 100; i++) {
    arr.push(
      <li className="category">
      <Image
      
      src="/categorias/cabine.svg"
      alt="categoria"
      width={14}
      height={14}
      
      />
      <label>Cabine</label>
      </li>
    )   
  }

  return arr;

}
const Reservation = () => {
  
  const [initalDate, setInitalDate] = useState(null);
  const [finalDate, setFinalDate] = useState(null);
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [numberPhone, setNumberPhone] = useState('');
  const [loading, setLoading] = useState(false);
  const [adultTotal, setAdultTotal] = useState(false);
  const [childrenTotal, setChildren] = useState(false);

  const load = () => {
      setLoading(true);

      setTimeout(() => {
          setLoading(false);
      }, 2000);
  };


  return (
    <div className="reservation">
      <div className="max-w-full">

        <div className="max-w-full relative filter">
            <h1 className="title">Categorias</h1>
        </div>
        <ul className="categories gap-5">
              { categories() }
        </ul>
        <div className="reservation-container">
            <div className="place">
              <h2 className="title">Luanda Place</h2>
              <h4 className="title subtitle">Cidade de Luanda, Angola</h4>
              <h4 className="title price">20 000 000,00 Kz/Noite</h4>
              <span className="description">
                Lorem ipsum dolor sit amet consectetur, 
                adipisicing elit. Sapiente, obcaecati excepturi 
                asperiores dolore veritatis fuga, nostrum tempore 
                quae odit earum dolores eaque eos ut nulla dignissimos 
                necessitatibus voluptatum ullam debitis!
              </span>
              <h4 className="title subtitle mt-5 ">Comodidades</h4>
                     {/* <ul className="commodities gap-5">
                    { commodities() }
                    </ul> */}
              <div className="place-card" style={{backgroundImage: 'url("/cidades/sample/1.jpg")'}}></div>
            </div>
            <div className="reserve">
              <div className="card"> 
                  <div className="card-row"> 
                      <div className="title">Faça agora a sua reserva </div>
                  </div>
                  <div className="card-row card-invert card-input">
                    <h4>Nome: </h4>
                    <InputText style={{width: 100 + '%'}} value={name} onChange={(e) => setName(e.target.value)} placeholder="Escreva aqui o seu nome" />
                  </div>
                  <div className="card-row card-input">
                    <h4>E-mail: </h4>
                    <InputText style={{width: 100 + '%'}} value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Escreva aqui o seu nome" />
                  </div>
                  <div className="card-row card-invert card-input">
                    <h4>Telefone:  </h4>
                    <InputMask style={{width: 100 + '%'}}  value={numberPhone} onChange={(e) => setNumberPhone(e.target.value)} mask="(+244) 999-999-999" placeholder="(+244) 999-999-999" />
                  </div>
                  <div className="card-row  card-input">
                    <h4>Total de crianças: </h4>
                    <InputNumber  
                        style={{width: 100 + '%'}} 
                        value={childrenTotal} 
                        onValueChange={(e: InputNumberValueChangeEvent) => setChildren(e.value)} 
                        showButtons 
                        buttonLayout="horizontal"
                        incrementButtonIcon="pi pi-plus" 
                        decrementButtonIcon="pi pi-minus"
                        min={0} max={100}
                        decrementButtonClassName="button-incremental" 
                        incrementButtonClassName="button-incremental decremental"
                    />
                  </div>
                  <div className="card-row card-invert card-input">
                      <h4>Total de adultos: </h4>
                      <InputNumber  
                          style={{width: 100 + '%'}} 
                          value={adultTotal} 
                          onValueChange={(e: InputNumberValueChangeEvent) => setAdultTotal(e.value)} 
                          showButtons 
                          buttonLayout="horizontal"
                          incrementButtonIcon="pi pi-plus" 
                          decrementButtonIcon="pi pi-minus"
                          min={0} 
                          max={100}
                          decrementButtonClassName="button-incremental" 
                          incrementButtonClassName="button-incremental decremental"
                      />
                  </div>
                  <div className="card-row  card-input">
                    <h4>Check In: </h4>
                    <Calendar 
                        style={{width: 100 + '%'}}  
                        value={initalDate} onChange={(e) => setInitalDate(e.value)} 
                        showIcon  
                        readOnlyInput 
                        showTime 
                        hourFormat="24" 
                    />
                  </div>
                  <div className="card-row card-invert card-input">
                    <h4>Check Out: </h4>
                    <Calendar  
                      style={{width: 100 + '%'}} 
                      value={finalDate} 
                      onChange={(e) => setFinalDate(e.value)} 
                      showIcon  
                      readOnlyInput 
                      showTime 
                      hourFormat="24" 
                    />
                  </div>
                  <div className="card-row  card-input">
                    <h4>Reservar: </h4>
                    <Button 
                      className="primary-button" 
                      label="Reservar" 
                      icon="pi pi-check" 
                      loading={loading} 
                      onClick={load} 
                    />
                  </div>
              </div>
            </div>
        </div>
      </div>
  </div>
  )
}

export default Reservation


 