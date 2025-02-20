import type { Meta, StoryObj } from '@storybook/react';
import { RAGProvider, ChatWindow, AdvancedQueryField, ErrorDisplay } from '../../lib/main';
import type { Message } from '../../lib/main';

const ExampleComponent = () => (
  <div style={{ width: '600px', height: '400px' }}>
    <RAGProvider
      retrieveAndGenerate={(messages: Message[]) => {
        // Example implementation returning promises
        return {
          sources: Promise.resolve([
            {
              sourceReference: "example-doc.pdf",
              type: "pdf" as const,
              metadata: {
                title: "Example Document"
              },
              relevanceScore: 1,
            }
          ]),
          response: Promise.resolve("This is a sample response based on the retrieved documents.")
        };
      }}
    >
      <div className="flex flex-col gap-4 h-full">
        <div className="flex-1">
          <ChatWindow />
        </div>
        <div>
          <AdvancedQueryField />
        </div>
      </div>
      <ErrorDisplay />
    </RAGProvider>
  </div>
);

const meta = {
  title: 'Tutorial/01. Basic Usage',
  component: ExampleComponent,
  parameters: {
    layout: 'centered',
    docs: {
      description: {
        component: `
# Basic Usage

This is the first step in learning how to use the RAG UI. Here you'll learn:
- Basic setup of the [RAGProvider](../?path=/docs/components-ragprovider--docs)
- How to implement a simple retrieveAndGenerate function
- Basic source and response handling

The simplest way to use the RAG UI is to implement the retrieveAndGenerate function. This function receives messages (containing the query and chat history) and should return both the retrieved sources and the generated response.

## Function Signature

\`\`\`typescript
{
  // Array of retrieved documents
  sources: Promise<{
    source: string,           // Document identifier
    type?: "pdf" | "html",    // Optional document type
    metadata?: {              // Optional metadata
      [key: string]: any
    },
    text?: string,           // Required if not using getDataSource
    relevanceScore?: number, // Optional relevance score
    highlights?: {            // Optional PDF highlights
      page: number,
      rect: { top: number, left: number, width: number, height: number },
      comment?: string
    }[]
  }[]>,
  response: Promise<string>   // The generated response
}
\`\`\`

## Example Implementation

\`\`\`tsx
<RAGProvider
  retrieveAndGenerate={(messages) => {
    return {
      sources: Promise.resolve([
        {
          source: "example-doc.pdf",
          type: "pdf",
          metadata: {
            title: "Example Document"
          },
          relevanceScore: 1
        }
      ]),
      response: Promise.resolve("This is a sample response based on the retrieved documents.")
    };
  }}
>
  <ChatWindow />
  <AdvancedQueryField />
</RAGProvider>
\`\`\`

Try out the example below to see the basic functionality in action.
Next, move on to "02. Source Types" to learn about different types of sources and how to handle them.
        `
      }
    }
  },
  tags: ['autodocs'],
} satisfies Meta<typeof ExampleComponent>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Docs: Story = {};