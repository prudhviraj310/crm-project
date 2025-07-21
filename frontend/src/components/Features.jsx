const Features = () => {
  return (
    <section className="py-16 bg-gray-100 text-center">
      <h3 className="text-3xl font-bold mb-8">Why Choose Our CRM?</h3>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 px-8">
        <div className="bg-white p-6 rounded-lg shadow">
          <h4 className="text-xl font-semibold mb-2">Client Management</h4>
          <p>Organize and track all your customers in one place.</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow">
          <h4 className="text-xl font-semibold mb-2">Sales Automation</h4>
          <p>Automate follow-ups and close deals faster.</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow">
          <h4 className="text-xl font-semibold mb-2">Analytics</h4>
          <p>Track performance with custom dashboards and reports.</p>
        </div>
      </div>
    </section>
  );
};

export default Features;
