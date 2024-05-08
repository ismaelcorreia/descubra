import React from 'react';

import Hero from '@/components/index/Hero.tsx';
import Reservation from '@/components/index/Reservation.tsx';


import Navbar from '@/components/Navbar';
import Footer from '@/components/Footer';

export default function Page()  {
  return (
    <>
        <Navbar/>
        <Hero/>
        <Reservation/>
        <Footer/>
    </>
  )
}
// "use client"
// import { useBearStore } from '@store';

// import Hero from '@/components/index/Hero.tsx';
// import Reservation from '@/components/index/Reservation.tsx';

// import '@/style/components.scss';

// export default function Home() {
  


//   return (

//     <div>
//       <Hero/>
//       <Reservation/>
//     </div>
   
//   );
// }

