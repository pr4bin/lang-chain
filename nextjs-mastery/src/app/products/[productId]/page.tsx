export default function ProductPage({ params }: { params: { productId: string } }) {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-4xl font-bold mb-4">
        Product ID: {params.productId}
      </h1>
      <p className="text-lg text-center">
        Details for product {params.productId} will go here.
      </p>
    </main>
  );
}
