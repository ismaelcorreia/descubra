import { User } from './user';
export interface Company {
    id: string;
    name: string;
    about: string;
    email: string;
    telephone: string;
    brand: string;
}
export interface Customer extends User {
    emblem: 'Normal' | 'Frequente' | 'Fiel' | 'Especial';
    discount: number;
}

