/* eslint-disable @next/next/no-img-element */
'use client';
import { useRouter } from 'next/navigation';
import React, { useContext, useState, useRef } from 'react';
import { Checkbox } from 'primereact/checkbox';
import { Button } from 'primereact/button';
import { Password } from 'primereact/password';
import { Steps } from 'primereact/steps';
import { MenuItem } from 'primereact/menuitem';
import { LayoutContext } from '../../../../layout/context/layoutcontext';
import { InputText } from 'primereact/inputtext';
import { classNames } from 'primereact/utils';
import { Toast } from 'primereact/toast';
import { FileUpload } from 'primereact/fileupload';
import { ProgressBar } from 'primereact/progressbar';
import { Tooltip } from 'primereact/tooltip';
import { SelectButton } from 'primereact/selectbutton';
import { Tag } from 'primereact/tag';
import { MultiStateCheckbox } from 'primereact/multistatecheckbox';

const RegisterPage = () => {
    const { layoutConfig } = useContext(LayoutContext);
    const stepperRef = useRef(null);

    const router = useRouter();
    const containerClassName = classNames('surface-ground flex align-items-center justify-content-center min-h-screen min-w-screen overflow-hidden', { 'p-input-filled': layoutConfig.inputStyle === 'filled' });

    return (
        <div className={containerClassName}>
            <div className="flex flex-column align-items-center justify-content-center">
                <img src={`/layout/images/logo-${layoutConfig.colorScheme === 'light' ? 'dark' : 'white'}.svg`} alt="Travel Finder" width={200 + 'px'} className="mb-5 flex-shrink-0" />
                <div
                    style={{
                        borderRadius: '56px',
                        padding: '0.3rem',
                        background: 'linear-gradient(180deg, var(--primary-color) 10%, rgba(33, 150, 243, 0) 30%)'
                    }}
                >
                    <div className="w-full surface-card py-2 px-5 sm:px-8" style={{ borderRadius: '53px' }}>
                        <div className="text-center mb-5">
                            <div className="text-900 text-3xl font-medium mb-3">Abertura de conta</div>
                        </div>
                        {Stepper()}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default RegisterPage;


const Stepper = function () {
    const [activeIndex, setActiveIndex] = useState<number>(0);

    /** COMPANY */
    const toast = useRef(null);
    const [CompanyName, setCompanyName] = useState('');
    const [CompanyNIF, setCompanyNIF] = useState('');

    const itemRenderer = (item, itemIndex) => {
        const isActiveItem = activeIndex === itemIndex;
        const backgroundColor = isActiveItem ? 'var(--primary-color)' : 'var(--surface-b)';
        const textColor = isActiveItem ? 'var(--surface-b)' : 'var(--text-color-secondary)';

        return (
            <span
                className="inline-flex align-items-center justify-content-center align-items-center border-circle border-primary border-1 h-3rem w-3rem z-1 cursor-pointer"
                style={{ backgroundColor: backgroundColor, color: textColor, marginTop: '-25px' }}
                onClick={() => setActiveIndex(itemIndex)}
            >
                <i className={`${item.icon} text-xl`} />
            </span>
        );
    };

    const items: MenuItem[] = [
        {
            icon: 'fi fi-rr-user',
            template: (item) => itemRenderer(item, 0)
        },
        {
            icon: 'fi fi-rr-city',
            template: (item) => itemRenderer(item, 1)
        },
        {
            icon: 'pi pi-check',
            template: (item) => itemRenderer(item, 2)
        }
    ];

    const incrementTab = () => {
        setActiveIndex(activeIndex + 1);
        console.log(activeIndex)
    }


    const displayTab = (index: number) => {
        return index === 0 ?
                UserRegisterPanel():
            index === 1 ?
                CompanyPanel():
                RegisterConfirmationPanel()
    }

    const RegisterConfirmationPanel = () => {

        return (
            <>
                <div>

                    <div className="flex  w-full md:w-30rem mt-5">
                        <h4  className=" text-900 text-xxl font-medium ">
                        Confirmação
                        </h4>

                    </div>


                </div>
            </>
        );
    };

    const CompanyPanel = () => {
        const fileUploadRef = useRef(null);
        const [CompanyBrand, setCompanyBrand] = useState(null);

        const [CompanyType, setCompanyType] = useState('Hotel');
        const typeOptions = [
            { icon: 'fi fi-ss-hotel', value: 'Hotel' },
            { icon: 'fi fi-sr-house-flood', value: 'Risort' },
            { icon: 'fi fi-sr-fireplace', value: 'Pousada' }
        ];

        const chooseOptions = { icon: 'pi pi-fw pi-images', iconOnly: true, className: 'custom-choose-btn p-button-rounded p-button-outlined' };

        const onSelectBrand = (e) => {
            toast.current.show({ severity: 'info', summary: 'Carregamento concluído', detail: 'Imagem carregada com sucesso' });
            console.log(fileUploadRef.current.getUploadedFiles())
        };

        const companyTypeTemplate = (option) => {
            return <span className="flex gap-2">
                <i className={option.icon}></i>
                <label >{option.value}</label>
            </span>;
        };

        return (
            <>
                <Toast ref={toast}></Toast>
                <Tooltip target=".custom-choose-btn" content="Clica para carregar a imagem" position="right" />
                <div>

                    <div className="flex  w-full md:w-30rem mt-5">
                        <h4  className=" text-900 text-xxl font-medium ">
                        Dados da Empresa
                        </h4>

                    </div>


                    <div className="card flex-row justify-content-center align-items-center ">

                    <label htmlFor="companyType" className="block text-900 text-xl font-medium mb-2">
                        Tipo de Empresa
                    </label>

                    <div className="flex  w-full md:w-30rem mb-5">
                        <SelectButton id="companyType" value={CompanyType} onChange={(e) => setCompanyType(e.value)} itemTemplate={companyTypeTemplate} optionLabel="value" options={typeOptions} />
                    </div>
                    <label htmlFor="companyName" className="block text-900 text-xl font-medium mb-2">
                        Nome da empresa
                    </label>
                    <InputText id="companyName" type="text" placeholder="Escreva o nome comercial da sua empresa" className="w-full md:w-30rem mb-5" style={{ padding: '1rem' }} />

                    <label htmlFor="companyNIF" className="block text-900 text-xl font-medium mb-2">
                        NIF da empresa
                    </label>
                    <InputText id="companyNIF" type="text" placeholder="Escreva o nif da sua empresa" className="w-full md:w-30rem mb-5" style={{ padding: '1rem' }} />

                    <label htmlFor="companyBrand" className="block text-900 text-xl font-medium mb-2">
                        Logotipo da empresa
                    </label>
                    <FileUpload id="companyBrand" ref={fileUploadRef} mode="basic" name="companyBrand" accept="image/*" maxFileSize={1000000} chooseOptions={chooseOptions} onSelect={onSelectBrand} />
                    </div>

                    <div className="flex flex-row gap-2 justify-content-end w-full md:w-30rem mt-5">
                        <Button label="Anterior" text tooltip="Voltar para o perfil" />
                        <Button label="Próximo" text tooltip="Avançar para o registo" />
                    </div>
                </div>
            </>
        );
    };

    const UserRegisterPanel = () => {
        const [Name, setName] = useState('');
        const [Email, setEmail] = useState('');
        const [password, setPassword] = useState('');
        const [passwordConfirm, setPasswordConfirm] = useState('');
        const profileImageRef = useRef(null);
        return (
            <div>
                <label htmlFor="name" className="block text-900 text-xl font-medium mb-2">
                Nome
                </label>
                <InputText id="name" type="text" placeholder="Digite o seu nome completo" className="w-full md:w-30rem mb-5" style={{ padding: '1rem' }} />
                <label htmlFor="email" className="block text-900 text-xl font-medium mb-2">
                    E-mail
                </label>
                <InputText id="email" type="text" placeholder="Email address" className="w-full md:w-30rem mb-5" style={{ padding: '1rem' }} />

                <label htmlFor="password" className="block text-900 font-medium text-xl mb-2">
                    Senha
                </label>
                <Password inputId="password" value={password} onChange={(e) => setPassword(e.target.value)}
                placeholder="Entre com uma senha forte" toggleMask className="w-full mb-5" inputClassName="w-full p-3 md:w-30rem"

                promptLabel="Digite uma senha" weakLabel="Senha fraca" mediumLabel="Senha mediana" strongLabel="Senha forte"

                ></Password>

<label htmlFor="confirmPassword" className="block text-900 font-medium text-xl mb-2">
                    Confirme a senha
                </label>
                <Password inputId="confirmPassword" value={passwordConfirm} onChange={(e) => setPasswordConfirm(e.target.value)}
                placeholder="Entre com uma senha forte" toggleMask className="w-full mb-5" inputClassName="w-full p-3 md:w-30rem"

                feedback={false}
                ></Password>


                <Button label="Próximo" className="w-full p-3 text-xl" onClick={incrementTab}></Button>
            </div>
        );
    };

    return (
        <div>
            <Steps model={items} activeIndex={activeIndex} readOnly={false} className="m-2 pt-4" />
            {displayTab(activeIndex)}
        </div>
    );
};
