/**
 * API Route Example
 * 
 * Why needed: This demonstrates how to create API endpoints in Next.js.
 * API routes allow you to handle HTTP requests, connect to databases,
 * and provide backend functionality for your frontend.
 */

import { NextResponse } from 'next/server'  // Next.js response helper

/**
 * GET endpoint - handles GET requests to /api/hello
 * Why needed: Demonstrates how to create a simple API endpoint
 * that returns JSON data
 */
export async function GET() {
  return NextResponse.json({ message: 'Hello from the API!' })
}

/**
 * POST endpoint - handles POST requests to /api/hello
 * Why needed: Shows how to handle form submissions, process data,
 * and return responses with the received data
 * @param request - The incoming HTTP request
 */
export async function POST(request: Request) {
  // Parse the JSON body from the request
  const body = await request.json()
  
  // Return a JSON response with the received data
  return NextResponse.json({ 
    message: 'Data received!',
    data: body  // Echo back the received data
  })
} 