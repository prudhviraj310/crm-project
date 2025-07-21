import { useState } from "react";
import { registerUser } from "../api/userApi";
import { toast } from "react-toastify";
import { useNavigate } from "react-router-dom";

export default function Register() {
  const [form, setForm] = useState({ name: "", email: "", password: "" });
  const navigate = useNavigate();

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await registerUser(form);
      toast.success("Registered successfully!");
      navigate("/login");
    } catch (err) {
      toast.error(err.response?.data?.detail || "Registration failed");
    }
  };

  return (
    <div className="max-w-md mx-auto mt-20 p-6 shadow-lg rounded bg-white">
      <h2 className="text-2xl font-bold mb-4 text-center">Register</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          name="name"
          onChange={handleChange}
          value={form.name}
          className="w-full p-2 border"
          placeholder="Name"
        />
        <input
          name="email"
          onChange={handleChange}
          value={form.email}
          className="w-full p-2 border"
          placeholder="Email"
        />
        <input
          type="password"
          name="password"
          onChange={handleChange}
          value={form.password}
          className="w-full p-2 border"
          placeholder="Password"
        />
        <button className="bg-blue-600 text-white px-4 py-2 rounded w-full">
          Register
        </button>
      </form>
    </div>
  );
}
