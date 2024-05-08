export interface Login {
    email: string;
    password: string;
}
export interface User {
    id: string;
    name: string;
    email: string;
    picture: string;
    gender: 'Masculino' | 'Feminino';
    birthDate: Date;
}
