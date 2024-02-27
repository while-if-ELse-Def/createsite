import React from 'react'; 
import { createRoot } from 'react-dom/client';  
import CertList from './components/cert'

const rootElement = document.getElementById('root');
if (rootElement) {
    createRoot(rootElement).render(<CertList />);
}