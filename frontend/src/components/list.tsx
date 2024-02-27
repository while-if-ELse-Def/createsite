import React from 'react';
import Cert from './cert'

export default function CertList(props: any) {
    const data = [
        { name: "Молочная ванна", price: 200, description: "Офигенная ванна"},
        { name: "Путешествие", price: 300, description: "Путешествие в никуда"},
        { name: "Книга", price: 100, description: "Книга для чтения"},
        { name: "Концерт", price: 500, description: "Билет на концерт"},
        { name: "Картина", price: 1000, description: "Картина для дома"},
        { name: "Кофе", price: 50, description: "Кофе для бодрости"},
    ]
    
    return (
        <div>
        {data.map((item) => (
            <Cert {...item} />
        ))}
    </div>
    );
}

