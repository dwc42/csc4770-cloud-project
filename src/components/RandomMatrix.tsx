import { useState } from "react";

export default function RandomMatrix() {
	const [nRowSize, setNRowSize] = useState<number>();
	const [mRowSize, setMRowSize] = useState<number>();
	const [matrix, setMatrix] = useState<number[][]>();
	return <div>
		<input />
		<input />
		<button onClick={() => {
			Array(nRowSize).map(() => {
				return Array(mRowSize).map(() => {

				});
			});
			setMatrix();
		}}>Randomize Matrix</button>
	</div>;
}