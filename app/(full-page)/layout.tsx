import { Metadata } from 'next';
// import AppConfig from '../../layout/AppConfig';
import React from 'react';

import '@flaticon/flaticon-uicons/css/all/all.css';
interface SimpleLayoutProps {
    children: React.ReactNode;
}

export const metadata: Metadata = {
    title: 'Travel Finder',
    description: 'Viaje com confiança.'
};

export default function SimpleLayout({ children }: SimpleLayoutProps) {
    return (
        <React.Fragment>
            {children}
            {/* <AppConfig simple /> */}
        </React.Fragment>
    );
}
