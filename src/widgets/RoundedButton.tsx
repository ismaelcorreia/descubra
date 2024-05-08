import Image from 'next/image';

type Props = {
    type: 'button' | 'submit';
    title: string;
    icon?: string;
    variant: 'btn_dark_green'
}

const RoundedButton = ({
    type,
    title,
    icon,
    variant
}: Props)=> {
  return (
    <button 
    className={`flexCenter border ${variant} cursor-pointer`}
    type={type}
    style={{gap: 5 + 'px', borderRadius: 30 + 'px'}}
    >
        {icon && <Image src={icon} alt={title} width={18} height={18} />}
        <label className="bold-16 whitespace-nowrap cursor-pointer">{title}</label>

    </button>
  )
}

export default RoundedButton