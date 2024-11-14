export const predict = async (inputData) => {
    try {
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(inputData),
        });
        return response.json();
    } catch (error) {
        console.error("Error:", error);
    }
};
