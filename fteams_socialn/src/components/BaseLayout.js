import React from 'react';
import Navbar from './Navbar';

function BaseLayout({ children }) {
    return (
        <div>
            <Navbar />
            <div className="container mt-7"> {/* Agrega un margen top para dar espacio al contenido */}
                <div className="row">
                    <div className="col">
                        {children}
                    </div>
                </div>
            </div>
        </div>
    );
}

export default BaseLayout;