/* eslint-disable @next/next/no-img-element */
"use client"
import Link from 'next/link';
import { classNames } from 'primereact/utils';
import React, { forwardRef, useContext, useImperativeHandle, useRef } from 'react';
import { AppTopbarRef } from '@/types';
import { LayoutContext } from './context/layoutcontext';
import { PrimeReactContext } from 'primereact/api';

const AppTopbar = forwardRef<AppTopbarRef>((props, ref) => {
    const { layoutConfig, setLayoutConfig, layoutState, onMenuToggle, showProfileSidebar } = useContext(LayoutContext);
    const menubuttonRef = useRef(null);
    const topbarmenuRef = useRef(null);
    const topbarmenubuttonRef = useRef(null);
    const darkmodeRef = useRef(false);
    const { setRipple, changeTheme } = useContext(PrimeReactContext);

    useImperativeHandle(ref, () => ({
        menubutton: menubuttonRef.current,
        topbarmenu: topbarmenuRef.current,
        topbarmenubutton: topbarmenubuttonRef.current
    }));

    const _changeTheme = () => {
        darkmodeRef.current=!darkmodeRef.current;
        let theme: string, colorScheme: string;


        if (!darkmodeRef.current){
            theme ='lara-light-teal';
            colorScheme = 'light';
        } else {
            theme ='lara-dark-teal';
            colorScheme = 'dark';
        }

        changeTheme?.(layoutConfig.theme, theme, 'theme-css', () => {
            setLayoutConfig((prevState: LayoutConfig) => ({ ...prevState, theme, colorScheme }));
        });
    };



    return (
        <div className="layout-topbar">
            <Link href="/" className="layout-topbar-logo">
                <img src={`/layout/images/logo-${layoutConfig.colorScheme !== 'light' ? 'white' : 'dark'}.svg`} height={'35px'} alt="logo" />
            </Link>

            <button ref={menubuttonRef} type="button" className="p-link layout-menu-button layout-topbar-button" onClick={onMenuToggle}>
                <i className="pi pi-bars" />
            </button>

            <button ref={topbarmenubuttonRef} type="button" className="p-link layout-topbar-menu-button layout-topbar-button" onClick={showProfileSidebar}>
                <i className="pi pi-ellipsis-v" />
            </button>

            <div ref={topbarmenuRef} className={classNames('layout-topbar-menu', { 'layout-topbar-menu-mobile-active': layoutState.profileSidebarVisible })}>
                <button type="button" className="p-link layout-topbar-button">
                    <i className="pi pi-calendar"></i>
                    <span>Calendar</span>
                </button>
                <button type="button" className="p-link layout-topbar-button">
                    <i className="pi pi-user"></i>
                    <span>Profile</span>
                </button>
                <button type="button" className="p-link layout-topbar-button" onClick={() => _changeTheme()}>
                    <i className={`pi ${darkmodeRef.current?"pi-moon":"pi-sun"}`}></i>
                    <span>{darkmodeRef.current?"Modo Claro":"Modo Escuro"}</span>
                </button>
                <button type="button" className="p-link layout-topbar-button">
                    <i id="themIcon" className="pi pi-cog"></i>
                    <span>Settings</span>
                </button>
            </div>
        </div>
    );
});

AppTopbar.displayName = 'AppTopbar';

export default AppTopbar;
