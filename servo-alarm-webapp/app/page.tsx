'use client';

import { useState, useEffect } from 'react';
import io from 'socket.io-client';

export default function Home() {
  const [alarmTime, setAlarmTime] = useState('');
  const [isConnected, setIsConnected] = useState(false);
  const [socket, setSocket] = useState<any>(null);

  useEffect(() => {
    // Connect to WebSocket server
    const newSocket = io('ws://YOUR_PICO_IP:8080');
    
    newSocket.on('connect', () => {
      setIsConnected(true);
      console.log('Connected to Pico W');
    });

    newSocket.on('disconnect', () => {
      setIsConnected(false);
      console.log('Disconnected from Pico W');
    });

    setSocket(newSocket);

    return () => {
      newSocket.close();
    };
  }, []);

  const handleSetAlarm = () => {
    if (socket && alarmTime) {
      socket.emit('setAlarm', { time: alarmTime });
      alert(`Alarm set for ${alarmTime}`);
    }
  };

  return (
    <main className="min-h-screen p-8 bg-gray-100">
      <div className="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl p-6">
        <h1 className="text-2xl font-bold mb-6 text-center">Servo Alarm Control</h1>
        
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            Set Alarm Time
          </label>
          <input
            type="time"
            value={alarmTime}
            onChange={(e) => setAlarmTime(e.target.value)}
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          />
        </div>

        <button
          onClick={handleSetAlarm}
          disabled={!isConnected}
          className={`w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded ${
            !isConnected ? 'opacity-50 cursor-not-allowed' : ''
          }`}
        >
          {isConnected ? 'Set Alarm' : 'Connecting...'}
        </button>

        <div className="mt-4 text-center">
          <p className={`text-sm ${isConnected ? 'text-green-500' : 'text-red-500'}`}>
            {isConnected ? 'Connected to Pico W' : 'Disconnected'}
          </p>
        </div>
      </div>
    </main>
  );
} 