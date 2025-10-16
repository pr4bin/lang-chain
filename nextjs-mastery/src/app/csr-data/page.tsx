"use client";

import { useState, useEffect } from "react";

export default function CSRDataPage() {
  const [dateTime, setDateTime] = useState<string | null>(null);

  useEffect(() => {
    const fetchDateTime = async () => {
      // Simulate fetching data from an API
      const response = await new Promise<string>((resolve) =>
        setTimeout(() => {
          resolve(new Date().toLocaleString());
        }, 500)
      );
      setDateTime(response);
    };

    fetchDateTime();

    // Fetch a new random number every 3 seconds
    const intervalId = setInterval(fetchDateTime, 1000);

    // Cleanup function to clear the interval when the component unmounts
    return () => clearInterval(intervalId);
  }, []); // Empty dependency array means this effect runs once on mount

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-4xl font-bold mb-4">Client-Side Rendered Data</h1>
      <p className="text-2xl text-center mb-4">
        Date Time:{" "}
        <span className="font-mono text-green-600 dark:text-green-400">
          {dateTime !== null ? dateTime : "Loading..."}
        </span>
      </p>
      <p className="text-lg text-gray-700 dark:text-gray-300 text-center">
        This data is fetched and updated on the client-side.
      </p>
    </main>
  );
}
