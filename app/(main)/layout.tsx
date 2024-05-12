import { Metadata } from 'next';
import Layout from '../../layout/layout';
import '@flaticon/flaticon-uicons/css/all/all.css';

interface AppLayoutProps {
    children: React.ReactNode;
}

export const metadata: Metadata = {
    title: 'Travel Finder',
    description: 'Viaje com confiança.',
    robots: { index: false, follow: false },
    viewport: { initialScale: 1, width: 'device-width' },
    icons: {
        icon: '/favicon.ico'
    }
};

export default function AppLayout({ children }: AppLayoutProps) {
    return <Layout>{children}</Layout>;
}
