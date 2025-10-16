import { notFound } from 'next/navigation';

interface Post {
  id: number;
  title: string;
  content: string;
  slug: string;
}

// Simulate a database or API call
const getPostBySlug = async (slug: string): Promise<Post | undefined> => {
  const posts: Post[] = [
    {
      id: 1,
      title: "My First Next.js Post",
      content: "This is the content of my very first blog post in Next.js. It was statically generated at build time!",
      slug: "my-first-nextjs-post",
    },
    {
      id: 2,
      title: "Understanding Server Components",
      content: "Server Components are a game-changer for performance and data fetching. They run on the server and reduce client-side JavaScript.",
      slug: "understanding-server-components",
    },
  ];
  return posts.find(post => post.slug === slug);
};

export default async function BlogPostPage({ params }: { params: { slug: string } }) {
  const post = await getPostBySlug(params.slug);

  if (!post) {
    notFound(); // Next.js utility to render a 404 page
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-5xl font-bold mb-6 text-center">
        {post.title}
      </h1>
      <p className="text-lg text-gray-700 dark:text-gray-300 max-w-2xl text-center">
        {post.content}
      </p>
      <p className="mt-8 text-sm text-gray-500">
        This page was statically generated (SSG).
      </p>
    </main>
  );
}

// This function tells Next.js which dynamic paths to pre-render at build time
export async function generateStaticParams() {
  const posts = [
    { slug: "my-first-nextjs-post" },
    { slug: "understanding-server-components" },
  ];
  return posts;
}
