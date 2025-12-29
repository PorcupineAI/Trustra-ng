export default function WhatsAppButton({ phone, message }) {
  const url = `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
  return (
    <a href={url} target="_blank" rel="noopener noreferrer">
      <button className="whatsapp-btn">
        Chat on WhatsApp
      </button>
    </a>
  );
}
