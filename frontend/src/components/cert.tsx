import React from 'react';

export default function Cert(props: any) {
    return (
      <div style={{width: '400px', height: '400px', border: '1px solid'}}>
        <div>{props.name}</div>
        <div>{props.price}</div>
        <div>{props.description}</div>
      </div>
      )
  }
//cert={name: "Молочная ванна", price=200,description="Офигенная ванна"}

