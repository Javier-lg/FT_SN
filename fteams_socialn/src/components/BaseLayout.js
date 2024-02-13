import React from 'react';
import Navbar from './Navbar';

function BaseLayout({ children }) {
    return (
        <div>
            <Navbar />
            <div className="container">
                {children}
            </div>
        </div>
    );
}

export default BaseLayout;