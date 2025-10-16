import Link from "next/link";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-6xl font-bold mb-8">
        My Next.js Mastery Journey Begins
      </h1>
      <div className="flex gap-4">
        <Link href="/about" className="text-blue-500 hover:underline text-xl">
          Go to About Page
        </Link>
        <Link
          href="/products/123"
          className="text-blue-500 hover:underline text-xl"
        >
          Go to Product 123
        </Link>
      </div>
    </main>
  );
}
