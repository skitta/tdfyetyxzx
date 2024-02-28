import axios from "axios";

axios.defaults.baseURL = `${window.location.protocol}//${window.location.host}/api`;
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8';

export interface Doctor {
    id: number,
    name: string,
    avatar: string,
    doctor_title: string,
    teacher_title: string,
    doctor_office: string,
    teacher_office: string,
    degree: string,
    field: string,
    info: string,
    link: string,
    major: string[],
    schedule: string[]
}

function getExperts(): Promise<Doctor[]> {
    return new Promise((resolve, reject) => {
        axios.get("/experts").then(response => {
            resolve(response.data);
        }).catch(error => {
            reject(error);
        })
    })
}

function getExpertById(id: number): Promise<Doctor> {
    return new Promise((resolve, reject) => {
        axios.get(`/experts/${id}`).then(response => {
            resolve(response.data);
        }).catch(error => {
            reject(error);
        })
    })
}

export {
    getExperts,
    getExpertById
}
