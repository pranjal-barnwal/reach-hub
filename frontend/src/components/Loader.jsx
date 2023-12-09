import React from 'react'

const Loader = () => {
    return (
        <div>
            <img
                src="https://i.gifer.com/origin/34/34338d26023e5515f6cc8969aa027bca_w200.webp"
                alt="Loading data..."
                width={80}
            />
            <p style={{ justifyContent: "center", fontWeight: "bold", }}>
                Loading...
            </p>
        </div>
    )
}

export default Loader