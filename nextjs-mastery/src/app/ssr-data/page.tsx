export default async function SSRDataPage() {
  const currentTime = new Date().toLocaleString();

  // Simulate a network delay to make the SSR effect more apparent
  await new Promise(resolve => setTimeout(resolve, 500));

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-4xl font-bold mb-4">
        Server-Side Rendered Data
      </h1>
      <p className="text-2xl text-center mb-4">
        Current Server Time: <span className="font-mono text-blue-600 dark:text-blue-400">{currentTime}</span>
      </p>
      <p className="text-lg text-gray-700 dark:text-gray-300 text-center">
        This page was rendered on the server for each request.
      </p>
    </main>
  );
}
