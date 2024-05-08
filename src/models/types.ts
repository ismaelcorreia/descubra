export interface Company {
    id: string;
    name: string;
    about: string;
    contact: {
        email: string;
        telephone: string;
    };
    brand: string;
    users: User[];
}
export interface PlaceType {
    id: string;
    name: string;
    image: string;
}
export interface PlaceCategory {
    id: string;
    name: string;
    image: string;
}

export interface PlaceConvenience{
    id: string;
    name: string;
    image: string;
}

export interface PlaceRule{
    id: string;
    name: string;
    image: string;
}

export interface Place {
    id: string;
    name: string;
    description: string;
    images: string[];
    type: PlaceType;
    categories: PlaceCategory[];
    stars: number;
    rooms: number;
    bathrooms: number;
    conveniences: PlaceConvenience[];
    rules: PlaceRule[];
    company: Company;
    season: 'Hora' | 'Noite' | 'Diária' | 'Mensal' | 'Anual';
    price: number;
    reservationPrice: number;
    oldPrice: number | null;
    lat: string;
    long: string;
    status: 'Disponível' | 'Ocupado'
}

export interface Host {
    id: string;
    place: Place;
    host: User;
    checkin: Date;
    checkout: Date;
    cost: number;
    season: string;
    duration: number;
    images: string[];
    type: PlaceType;
    categories: PlaceCategory[];
    stars: number;
}

