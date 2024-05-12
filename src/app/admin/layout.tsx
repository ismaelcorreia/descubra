

// import { PrimeReactProvider } from 'primereact/api';

// import "primereact/resources/themes/saga-green/theme.css";
// import 'primeicons/primeicons.css';
// import "@/app/globals.css";
// import "@/style/main.scss"
// import { useBearStore } from '@store';



export default function AdminLayout({
  children
}:  {
  children: React.ReactNode
}) {

  return (

    <>

    <div>Hello</div>
        <main>{children}</main>
    </>
  );
}

