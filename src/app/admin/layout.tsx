

// import { PrimeReactProvider } from 'primereact/api';

// import "primereact/resources/themes/saga-green/theme.css";
// import 'primeicons/primeicons.css';
// import "@/app/globals.css"; 
// import "@/style/main.scss"
// import { useBearStore } from '@store';

import "primereact/resources/themes/saga-green/theme.css";
import 'primeicons/primeicons.css';
import "../globals.css"; 
import "@/style/main.scss"
import '@/style/components.scss';

import Menu from '@/components/admin/Menu'

export default function AdminLayout({
  children
}:  {
  children: React.ReactNode
}) {
  
  return ( 
    
    <>
    
    <Menu/>
        <main>{children}</main>
    </>
  );
}

