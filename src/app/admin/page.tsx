"use client"
import React, { useState } from 'react';

const AddPlaceForm = () => {
    const [place, setPlace] = useState({
        id: '',
        name: '',
        description: '',
        images: [],
        type: null,
        categories: [],
        stars: 0,
        rooms: 0,
        bathrooms: 0,
        conveniences: [],
        rules: [],
        company: null,
        season: '',
        price: 0,
        reservationPrice: 0,
        oldPrice: null,
        lat: '',
        long: '',
        status: ''
    });

    const handleInputChange = (e, name) => {
        const updatedPlace = { ...place, [name]: e.target.value };
        setPlace(updatedPlace);
    };

    const handleTypeChange = (e) => {
        const updatedPlace = { ...place, type: e.target.value };
        setPlace(updatedPlace);
    };

    const handleCategoryChange = (e) => {
        const updatedPlace = { ...place, categories: e.target.value.split(',') };
        setPlace(updatedPlace);
    };

    const handleSubmit = () => {
        // Handle form submission, e.g., send data to backend
        console.log('Submitted:', place);
    };

    return (
        <div className="max-w-xl mx-auto bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
            <div className="mb-4">
                <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="name">
                    Name
                </label>
                <input 
                    className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    id="name" 
                    type="text" 
                    value={place.name} 
                    onChange={(e) => handleInputChange(e, 'name')} 
                    placeholder="Name"
                />
            </div>
            <div className="mb-4">
                <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="description">
                    Description
                </label>
                <textarea 
                    className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    id="description" 
                    value={place.description} 
                    onChange={(e) => handleInputChange(e, 'description')} 
                    placeholder="Description"
                />
            </div>
            <div className="mb-4">
                <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="type">
                    Type
                </label>
                <select 
                    className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    id="type" 
                    value={place.type} 
                    onChange={handleTypeChange}
                >
                    <option value="">Select Type</option>
                    <option value="type1">Type 1</option>
                    <option value="type2">Type 2</option>
                </select>
            </div>
            <div className="mb-4">
                <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="categories">
                    Categories
                </label>
                <input 
                    className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    id="categories" 
                    type="text" 
                    value={place.categories} 
                    onChange={(e) => handleCategoryChange(e, 'categories')} 
                    placeholder="Category 1, Category 2"
                />
            </div>
            <div className="flex items-center justify-between">
                <button 
                    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" 
                    type="button"
                    onClick={handleSubmit}
                >
                    Submit
                </button>
            </div>
        </div>
    );
};

export default AddPlaceForm;

