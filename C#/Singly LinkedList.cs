using System;

namespace LinkedList_Practice
{
	class Program
	{
		static void Main(string[] args)
		{
			/** Start of an Integer LinkedList **/
			LinkedList linkedList = new LinkedList();
			linkedList.AddNode(1);
			linkedList.AddNode(2);
			linkedList.AddNode(6);
			linkedList.AddNode(3);
			linkedList.AddNode(4);
			linkedList.AddNode(5);
			linkedList.AddNode(6);
            linkedList.ShowNodes();
            linkedList.RemoveElements(6);

            // List - 1
            LinkedList llist1 = new LinkedList();
			llist1.AddNode(1);
			llist1.AddNode(2);
			llist1.AddNode(4);

			// List - 2
			LinkedList llist2 = new LinkedList();
			llist2.AddNode(1);
			llist2.AddNode(3);
			llist2.AddNode(4);
            Console.Write("Merged: ");
            llist1.MergedTwoLists(llist1.Head, llist2.Head);


            LinkedList nthLList = new LinkedList();
			nthLList.AddNode(1);
			nthLList.AddNode(2);
			nthLList.AddNode(3);
			nthLList.AddNode(4);
			nthLList.AddNode(5);
            nthLList.RemoveNthNodeFromEnd(2);

            LinkedList dupliLlist = new LinkedList();
			dupliLlist.AddNode(1);
			dupliLlist.AddNode(1);
			dupliLlist.AddNode(2);
			dupliLlist.AddNode(3);
			dupliLlist.AddNode(3);
			dupliLlist.RemoveDuplicates();


			/** Start of a String LinkedList **/
			//Head - A 
			StringLinkedList HeadA = new StringLinkedList();
			StringNode a1 = new StringNode("a1");
			StringNode a2 = new StringNode("a2");

			StringNode c1 = new StringNode("c1");
			StringNode c2 = new StringNode("c2");
			StringNode c3 = new StringNode("c3");

			//Creating the Chains
			a1.Next = a2;
			a2.Next = c1;
			c1.Next = c2;
			c2.Next = c3;

			//Making 'a1' the head of HeadA
			HeadA.Head = a1;

			//Head - B 
			StringLinkedList HeadB = new StringLinkedList();
			StringNode b1 = new StringNode("b1");
			StringNode b2 = new StringNode("b2");
			StringNode b3 = new StringNode("b3");

			//Creating the Chains
			b1.Next = b2;
			b2.Next = b3;
			b3.Next = c1;

			//Making 'b1' the head of HeadB
			HeadB.Head = b1;

			StringLinkedList sLlist = new StringLinkedList();
            sLlist.GetIntersectedNode(HeadA.Head, HeadB.Head);

        }
	}


	public class Node
	{
		public int Data { get; set; }
		public Node Next { get; set; }

		public Node(int data)
		{
			Data = data;
			Next = null;
		}
	}

	public class LinkedList
	{
		public Node Head { get; set; }

		public LinkedList()
		{
			Head = null;
		}

		public void AddNode(int data)
		{
			Node newNode = new Node(data);

			if (Head == null)
			{
				Head = newNode;
			}
			else
			{
				Node current = Head;
				while (current.Next != null)
				{
					current = current.Next;
				}
				current.Next = newNode;
			}
		}

		public void ShowNodes()
		{
			Node current = Head;

			while (current != null)
			{
				if (current.Next == null)
				{
					Console.WriteLine(current.Data);
				}
				else
				{
					Console.Write(current.Data + " --> ");
				}
				current = current.Next;
			}
		}

		public void RemoveElements(int val)
		{
			Node dummy = new Node(0);
			dummy.Next = Head;
			Node current = dummy;

			while (current.Next != null)
			{
				if (current.Next.Data == val)
				{
					current.Next = current.Next.Next;
				}
				else
				{
					current = current.Next;
				}
			}
			ShowNodes();
		}

		public void MergedTwoLists(Node llist1, Node llist2)
		{
			LinkedList mergedList = new LinkedList();
			Node dummy = new Node(0);
			Node tail = dummy;

			while (llist1 != null && llist2 != null)
			{
				if (llist1.Data < llist2.Data)
				{
					tail.Next = llist1;
					llist1 = llist1.Next;
				}
				else
				{
					tail.Next = llist2;
					llist2 = llist2.Next;
				}
				tail = tail.Next;
			}

			if (llist1 != null)
			{
				tail.Next = llist1;
			}
			else if (llist2 != null)
			{
				tail.Next = llist2;
			}
			ShowNodes();
		}

		public void RemoveNthNodeFromEnd(int n)
		{
			if (n <= 0)
			{
				return;
			}

			Node dummy = new Node(0);
			dummy.Next = Head;
			Node fast = dummy;
			Node slow = dummy;

			for (int i = 0; i < n; i++)
			{
				if (fast == null)
				{
					return;
				}

				fast = fast.Next;
			}

			while (fast.Next != null)
			{
				fast = fast.Next;
				slow = slow.Next;
			}

			slow.Next = slow.Next.Next;

			Head = dummy.Next;

			ShowNodes();
		}
		public void RemoveDuplicates()
		{
			Node current = Head;

			while (current != null && current.Next != null)
			{
				if (current.Data == current.Next.Data)
				{
					current.Next = current.Next.Next;
				}
				else
				{
					current = current.Next;
				}
			}

			ShowNodes();

		}


	}

	public class StringNode
	{
		public string Data { get; set; }
		public StringNode Next { get; set; }


		public StringNode(string data)
		{
			Data = data;
			Next = null;
		}

	}

	public class StringLinkedList
	{
		//Initialization
		public StringNode Head { get; set; }

		public StringLinkedList()
		{
			Head = null;
		}

		public void GetIntersectedNode(StringNode HeadA, StringNode HeadB)
		{
			StringNode pointerA = HeadA;
			StringNode pointerB = HeadB;

			while (pointerA != pointerB)
			{
				if (pointerA != null)
				{
					pointerA = pointerA.Next;
				}
				else
				{
					pointerA = HeadB;
				}

				if (pointerB != null)
				{
					pointerB = pointerB.Next;
				}
				else
				{
					pointerB = HeadA;
				}
			}

			if (pointerA != null)
			{
				Console.WriteLine($"Intersected at: {pointerA.Data}");
			}
			else
			{
				Console.WriteLine("No Intersection!");
			}

		}


	}

}

