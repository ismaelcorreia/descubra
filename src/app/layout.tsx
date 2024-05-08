
import type { Metadata } from "next";
import { PrimeReactProvider } from 'primereact/api';
import "primereact/resources/themes/saga-green/theme.css";
import 'primeicons/primeicons.css';
import "./globals.css"; 
import "@/style/main.scss"
import '@/style/components.scss';

export const metadata: Metadata = {
  title: "descubra!",
  description: "Faça uma viagem e descanse no melhor lugar da zona",
};

export default function IndexLayout({
  children,
}: {
  children: React.ReactNode
}) {
  
  return ( 

        <PrimeReactProvider>
          <html lang="pt">
            <body>
            {children}
            </body>
          </html> 
        </PrimeReactProvider>
  );
}


// import type { Metadata } from "next";
// import { PrimeReactProvider } from 'primereact/api';
// import "primereact/resources/themes/saga-green/theme.css";
// import 'primeicons/primeicons.css';
// import "../globals.css"; 
// import "@/style/main.scss"

// export const metadata: Metadata = {
//   title: "descubra!",
//   description: "Faça uma viagem e descanse no melhor lugar da zona",
// };

// export default function IndexLayout({
//   children,
// }: {
//   children: React.ReactNode
// }) {
  
//   return (
//         <PrimeReactProvider>
//           <html lang="pt">
//             <body>
//             {children}
//             </body>
//           </html>
//         </PrimeReactProvider>
//   );
// }

