import Link from "next/link";
import Image from "next/image";
import {NAV_LINKS as links} from "@/utils/constUtils";
import RoundedButton from '@/widgets/RoundedButton';

const Navbar = () => {
  
  return (
    <nav className="navbar flexBetween max-container padding-container relative z-30 py-5">
      <Link href="/">
          <Image src="/logo.svg" alt="logo" width={90} height={24}/>
      </Link>


      <ul className="hidden h-full gap-12 lg:flex">
        {
          

          links.map((link) => (
            <Link href={link.to} key={link.key} 
            className="regular-16 text-gray-50 flexCenter cursor-pointer pb-1.5 transition-all hover:font-bold hover:text-black hover:underline">
              {link.text}
              </Link>
          )
          
          
          )
          
        }
          </ul>

          <div className="lg:flexCenter hidden">
            <RoundedButton
            type="button"
            title="Entrar"
            icon="/user-white.svg"
            variant="btn_dark_green"
            
            />
          </div>

          <Image 
              src="/menu.svg" 
              alt="menu" 
              width={30} 
              height={39}
              className="inline-block cursor-pointer lg:hidden"

          />



    </nav>
  )
}

export default Navbar

 