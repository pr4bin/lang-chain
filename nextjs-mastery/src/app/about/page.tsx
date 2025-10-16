import Link from 'next/link';

export default function AboutPage() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-4xl font-bold mb-4">
        About Us
      </h1>
      <p className="text-lg text-center mb-8">
        This is the About page for our Next.js Mastery application.
      </p>
      <Link href="/" className="text-blue-500 hover:underline text-xl">
        Go to Homepage
      </Link>
    </main>
  );
}
